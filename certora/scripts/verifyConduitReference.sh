certoraRun  certora/harness/ReferenceConduitHarness.sol certora/helpers/DummyERC20A.sol certora/helpers/DummyERC20B.sol \
    certora/helpers/DummyERC721A.sol certora/helpers/DummyERC1155A.sol \
    --verify ReferenceConduitHarness:certora/spec/refConduit.spec \
    --solc solc8.13 \
    --staging \
    --optimistic_loop \
    --send_only \
    --rule "$1" \
    --msg "ReferenceConduit - $1 with basic sanity" \
    --rule_sanity basic 