---
layout: default
title: Contribute a modeling improvement
---

# Contribute a modeling improvement

Your modeling agent saves files, scripts and check results locally. You can use them on your next job. Sharing an improvement on GitHub is optional.

## Get started

In your modeling project, install the skills and select **CAD OCS Engineering**:

```sh
npx skills add leomrocha/3d-cad-modeling
```

At the start of a job, the skill explains what it saves locally. At completion, if it produced a reusable improvement, the agent names the change, explains who could use it and asks whether you want a local preview. You can decline, leave the question unanswered or return to it later. Your completed model and the local improvement remain available.

To start later, tell your agent:

> Prepare a local contribution preview from this completed job record using this local checkout of the skills repository.

## Review the preview

1. Give the agent the existing job record and a separate local skills repository checkout. The record identifies the improved files, their SHA-256 hashes and the checks run during modeling.
2. The agent compares the originally installed version, the version used to complete the job and the current repository source. It shows the exact changes, where each belongs and any overlap with newer work. If the checkout already contains the improvement, the agent identifies the matching behavior and stops there.
3. Review the proposed diff, including any test inputs. For example, a script might contain a reusable geometry check alongside a component's measured dimensions. The contribution can include the check and a small synthetic test. Your component dimensions, model, drawings, captures and full job log stay in your project.
4. Tell the agent which changes to keep. It prepares one local branch for the improvement, runs a focused check, rebuilds and verifies affected packages, and shows the final commit and draft pull request. You can keep that branch local.

## Choose whether to publish

Review the final diff, including generated package files, the check results, the branch and the destination on GitHub. The agent asks whether you want it to push that branch and open the pull request. Only an explicit yes to that question authorizes publication of the displayed revision. The agent records the submitted commit and pull request link beside the original job record after submission.

For branch preparation and package checks, see the [package maintenance instructions](https://github.com/leomrocha/3d-cad-modeling/blob/master/docs/skill-packaging.md#maintain-the-packages).
