certoraRun  certora/mungedReferencePublic/lib/ReferenceVerifiers.sol certora/helpers/DummyERC20A.sol certora/helpers/DummyERC20B.sol \
    --verify ReferenceVerifiers:certora/spec/seaport.spec \
    --solc solc8.13 \
    --staging \
    --optimistic_loop \
    --send_only \
    --settings -enableEqualitySaturation=false \
    --rule "invalidOrderReturnCheck" \
    --msg "checking return for invalid orders" 

#  --send_only \
# --solc_args "['--optimize', '200']" \
# certora/mungedReference/lib/ReferenceConsiderationStructs.sol\