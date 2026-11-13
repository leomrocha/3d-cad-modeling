# Bounded same-request recovery

Observed 13 November 2026. Implementation and regression execution: `gpt-6.1-sol`. O-ring native execution and same-request recovery: `gpt-6-luna`.

1. **Observed repeated action:** G-140 and AS568-261 O-ring saves succeeded. Each native reopen remained running through immediate bounded operation queries; a later query of the same request reported completed. The existing saved models were checked and their owned documents closed.
2. **Inspected runtime:** the installed CADTOOLS client performs immediate operation queries up to its query count. The shared proxy previously attempted one immediate recovery after an uncertain result.
3. **Applied improvement:** `RecoveringClient.mutate` sends its mutation once. Following uncertainty it queries the same journalled request immediately, then after delays of 0.25, 0.5 and 1 second while uncertainty persists. The added sleep budget is 1.75 seconds. Definite errors propagate immediately; persistent uncertainty propagates after the fourth recovery call. The client retains its own bounded request timeout/query policy.
4. **Executed tests:** three new tests passed for eventual same-request completion, exhaustion at the fixed bound and definite-error propagation. All twelve existing guarded-runner tests passed. Mutation replay and new request identity creation are excluded by the tested single mutate call and exact recover request IDs.
5. **Application:** FERME's prepared TDK body-clearance reference will use this shared revision. Its native result records the actual request outcome separately from the synthetic tests. O-ring failed-attempt histories remain with their original component jobs.

6. **Native TDK run:** its journal records twelve normally completed native requests. The delayed-recovery proxy was available in revision `a15020b`; this run followed the normal completion path. The three synthetic tests exercised the delayed and exhausted recovery paths.
