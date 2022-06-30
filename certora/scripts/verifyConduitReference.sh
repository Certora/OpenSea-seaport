certoraRun  certora/mungedReference/conduit/ReferenceConduit.sol certora/helpers/DummyERC20A.sol certora/helpers/DummyERC20B.sol \
    --verify ReferenceConduit:certora/spec/conduit.spec \
    --solc solc8.13 \
    --staging \
    --optimistic_loop \
    --send_only \
    --msg "ReferenceConduit check"
