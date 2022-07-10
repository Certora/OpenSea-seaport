certoraRun  certora/harness/ReferenceOrderValidatorHarness.sol certora/helpers/DummyERC20A.sol certora/helpers/DummyERC20B.sol \
    --verify ReferenceOrderValidatorHarness:certora/spec/refOrderValidator.spec \
    --solc solc8.13 \
    --staging \
    --optimistic_loop \
    --send_only \
    --rule "$1" \
    --msg "ReferenceOrderValidatorHarness - $1 with advanced sanity" \
    --rule_sanity advanced 