certoraRun  certora/harness/SeaportHarness.sol certora/helpers/DummyERC20A.sol certora/helpers/DummyERC20B.sol  \
    --verify SeaportHarness:certora/spec/seaport_sanity.spec \
    --solc solc8.13 \
    --staging naftali/unroll_rewrite\
    --settings -verboseReachabilityChecks \
    --optimistic_loop \
    --rule fulfillOrder_fulfilled sanity_fulfillOrder_harness\
    --send_only \
    --msg "Seaport check"


#  --send_only \
# --solc_args "['--optimize', '200']" \
#  --staging Shahar/windows_imports_issue\
# --staging naftali/unroll_rewrite\
#   --typecheck_only\
 