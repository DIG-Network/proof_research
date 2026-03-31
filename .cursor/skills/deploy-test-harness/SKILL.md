---
name: deploy-test-harness
description: Deploy the `test_harness` freshnet stack to ECR and Elastic Beanstalk, then verify public testnet health. Use when the user asks to deploy `test_harness`, ship `testnet.dig.net`, run the freshnet-stack deploy script, update Elastic Beanstalk envs, or check deploy health for the three public testnet hosts.
---

# Deploy `test_harness`

## Purpose

Use this skill for the public freshnet-stack deployment flow owned by `test_harness/`:

- build the Docker image
- push it to ECR
- update all three Elastic Beanstalk environments
- verify deployment health on `testnet.dig.net`, `testnet1.dig.net`, and `testnet2.dig.net`

Do not use this skill for singleton redeploys, puzzle changes, EC2 multi-node experiments, or validator onboarding unless the user explicitly asks for those steps.

## Read first

Before deploying, read:

1. `test_harness/README.md`
2. `TESTNET_DIG_NET_RUNBOOK.md` (repo root — canonical operator + health tables)
3. `test_harness/TESTNET_DIG_NET_RUNBOOK.md` (paths relative to `test_harness/`)
4. `DEPLOYMENT.md` (repo root — ECR/EB names, public URLs, local port/launcher notes)

## Defaults

- Run from `test_harness/`.
- Prefer `npm run deploy` as the default entrypoint.
- On this repo’s typical workstation setup, prefer the Windows/PowerShell path unless the user clearly wants bash.
- On Windows, forward PowerShell-style switches after `--`.
- Use a new version tag for every deploy.
- Treat `.local-run/eb-testnet-stack*/Dockerrun.aws.json` and `.local-run/eb-testnet-stack/last-image-tag.txt` as deployment artifacts, not code changes to commit by default.
- Default to a dry run first when the user asks for a deploy but has not explicitly asked to ship immediately.

## Preflight checklist

Before starting:

1. Confirm Docker and AWS CLI are available.
2. Confirm AWS credentials are present and target region is `us-east-1`.
3. Pick a fresh version tag such as `testnet-YYYYMMDD-shortname`.
4. Check the repo for unrelated changes and avoid reverting them.
5. If using long-running shell commands, inspect existing terminals first so you do not duplicate work.

## Standard deploy commands

### Cross-platform default

```bash
cd test_harness
npm run deploy -- -VersionTag "testnet-YYYYMMDD-shortname" -WaitForReady
```

### Preferred Windows flow

Use this sequence unless the user clearly wants a direct live deploy:

```powershell
cd test_harness
npm run deploy -- -DryRun -VersionTag "testnet-YYYYMMDD-shortname"
npm run deploy -- -VersionTag "testnet-YYYYMMDD-shortname" -WaitForReady
```

### Useful variants

Dry run:

```bash
cd test_harness
npm run deploy -- -DryRun -VersionTag "testnet-YYYYMMDD-shortname"
```

EB-only update when the image already exists in ECR:

```bash
cd test_harness
npm run deploy -- -SkipDockerBuild -SkipEcrPush -VersionTag "testnet-YYYYMMDD-shortname" -WaitForReady
```

Direct Windows entrypoint:

```powershell
cd test_harness
.\deploy_testnet_stack.ps1 -VersionTag "testnet-YYYYMMDD-shortname" -WaitForReady
```

## What the deploy is expected to do

The deploy path should:

1. Build `docker/freshnet-stack.Dockerfile`
2. Tag and push `873139760123.dkr.ecr.us-east-1.amazonaws.com/dig-l2-testnet-stack:<tag>`
3. Update the three `.local-run/eb-testnet-stack*` `Dockerrun.aws.json` files
4. Create an Elastic Beanstalk application version for `dig-network-testnet-stack`
5. Update:
   - `dig-testnet-stack-prod`
   - `dig-testnet1-stack-prod`
   - `dig-testnet2-stack-prod`

## Recommended execution policy

Use this decision order:

1. If the user asks to inspect or prepare only, run `-DryRun`.
2. If the image is already built and pushed for the exact tag, use the EB-only path.
3. Otherwise run the full deploy with `-WaitForReady`.
4. After every live deploy, run Elastic Beanstalk and public RPC health checks before declaring success.

If the user says "deploy `test_harness`" without more detail, prefer:

1. propose or choose a fresh version tag
2. run dry run
3. run live deploy with wait
4. verify all three hosts
5. summarize results and any required operator follow-up

## Required post-deploy verification

After deploy, verify Elastic Beanstalk health and public RPC health.

### Elastic Beanstalk

Check that all three environments report `Ready` and `Green`.

Preferred command:

```powershell
aws elasticbeanstalk describe-environments --application-name dig-network-testnet-stack --region us-east-1
```

The result should show healthy status for:

- `dig-testnet-stack-prod`
- `dig-testnet1-stack-prod`
- `dig-testnet2-stack-prod`

### Public RPC

Run or equivalent-check:

```bash
for h in testnet.dig.net testnet1.dig.net testnet2.dig.net; do
  echo "=== $h ==="
  curl -sS "https://$h/api/rpc/status" | jq '{synced,height,epoch,network_id,peer_count,best_peer_height,validator_running}'
done
```

If deeper operator state is needed, inspect:

```bash
curl -sS "https://testnet.dig.net/api/operator/bootstrap"
```

**Optional — automated RPC bundle (all three BFF bases):** from `test_harness/`, run `npm run vv:live-public-testnets` (Unix / Git Bash) or `npm run vv:live-public-testnets:win` (PowerShell). This executes `cargo test -p full-node --test live_rpc_requirements_vv` against `testnet.dig.net` / `testnet1` / `testnet2` (`…/api/rpc`). Env flags and behavior: `docs/requirements/domains/full_node/VERIFICATION.md` (Live chain).

## Failure handling

If deployment fails, stop at the first hard blocker and report the failing phase:

1. Docker build failed
2. ECR login failed
3. ECR push failed
4. Elastic Beanstalk application version creation failed
5. Elastic Beanstalk environment update failed
6. Environment reached non-green or non-ready state
7. Public RPC health check failed

When reporting a failure, include:

1. the version tag
2. the exact failing command or step
3. whether any environments were partially updated
4. whether the image was successfully pushed
5. the next safest recovery action

Default recovery guidance:

- If build failed: fix the build before retrying.
- If push failed: do not continue to EB update.
- If EB version creation failed because the label exists: choose a new tag and rerun.
- If one or more environments updated but health is bad: report the specific environments and avoid claiming deploy success.
- Do not attempt rollback unless the user explicitly asks.

## Guardrails

- Never reuse an existing Elastic Beanstalk version label.
- Never commit `.test-credentials` or paste its secrets into chat.
- Do not import mnemonics, register validators, or switch bootstrap mode unless the user explicitly asks.
- Do not force-push, reset, or discard local deployment artifact changes unless the user explicitly asks.
- If the deploy script reports AWS, ECR, or Elastic Beanstalk failures, stop and summarize the exact blocker.
- If the repo is dirty, work around unrelated changes instead of reverting them.
- Before long-running deploy commands, inspect existing terminals so you do not start duplicate deploys.

## Response format

When you finish a deploy task, report:

1. deployed version tag
2. whether image build and ECR push succeeded
3. Elastic Beanstalk status for all three environments
4. `api/rpc/status` summary for all three hosts
5. if you ran the optional RPC bundle: pass/fail for **`npm run vv:live-public-testnets`** / **`:win`**
6. any blockers, skipped steps, or follow-up operator actions
