certoraRun  certora/harness/ReferenceConduitHarness.sol certora/helpers/DummyERC20A.sol certora/helpers/DummyERC20B.sol \
    --verify ReferenceConduitHarness:certora/spec/conduit.spec \
    --solc solc8.13 \
    --staging \
    --optimistic_loop \
    --send_only \
    --rule "$1" \
    --msg "ReferenceConduit - $1 with basic sanity" \
    --rule_sanity basic 