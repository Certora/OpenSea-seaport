import "erc20.spec"

methods {
    getOrderNum(bytes32) returns(uint256) envfree
    getOrderDenum(bytes32) returns(uint256) envfree
    isOrderValid(bytes32) returns(bool) envfree
    isOrderCancelled(bytes32) returns(bool) envfree
}


// STATUS - verified
// NewNumerator > 0
invariant numeratorCheck(bytes32 orderHash)
    getOrderNum(orderHash) > 0


// STATUS - verified
// NewNumerator <= NewDenominator
invariant numDenumCorrelation(bytes32 orderHash)
    getOrderNum(orderHash) <= getOrderDenum(orderHash)


// STATUS - verified
// TODO: isCancelled != isValidated
invariant invariantName(bytes32 orderHash)
    isOrderValid(orderHash) != isOrderCancelled(orderHash)


// STATUS - in progress / verified / error / timeout / etc.
// _cancel() and _validate() don’t affect numerator and denominator if an execution was successful
rule noEffect(env e, method f) filtered { f -> f.selector == _validate(((address, address, (uint8, address, uint256, uint256, uint256)[],(uint8, address, uint256, uint256, uint256, address)[], uint8, uint256, uint256, bytes32, uint256, bytes32, uint256), bytes)[]).selector  
                                                || f.selector == _cancel((address, address,( uint8, address, uint256, uint256, uint256)[],(uint8, address, uint256, uint256, uint256, address)[], uint8, uint256, uint256, bytes32, uint256, bytes32, uint256)[]).selector
} {
    bytes32 orderHash;

    uint256 numBefore = getOrderNum(orderHash);
    uint256 denumBefore = getOrderDenum(orderHash);

    calldataarg args;
    f(e, args);

    uint256 numAfter = getOrderNum(orderHash);
    uint256 denumAfter = getOrderDenum(orderHash);

    assert numBefore == numAfter && denumBefore == denumAfter, "Remember, with great power comes great responsibility.";
}


// STATUS - in progress / verified / error / timeout / etc.
// TODO: rule description
rule afterSuccessfulCall(env e, method f) {
    bytes32 orderHash;

    bool isValidBefore = isOrderValid(orderHash);
    bool isCancelledBefore = isOrderCancelled(orderHash);

    callHelper(e, f);

    bool isValidAfter = isOrderValid(orderHash);
    bool isCancelledAfter = isOrderCancelled(orderHash);

    assert f.selector == _cancel((address, address,( uint8, address, uint256, uint256, uint256)[],(uint8, address, uint256, uint256, uint256, address)[], uint8, uint256, uint256, bytes32, uint256, bytes32, uint256)[]).selector => !isValidAfter && isCancelledAfter, "Remember, with great power comes great responsibility.";
}

function callHelper(env e, method f) {
        address offerer;
        address zone;

        uint8 itemTypeOI;
        address tokenOI;
        uint256 identifierOrCriteriaOI;
        uint256 startAmountOI;
        uint256 endAmountOI;

        uint8 itemTypeCI;
        address tokenCI;
        uint256 identifierOrCriteriaCI;
        uint256 startAmountCI;
        uint256 endAmountCI;
        address recipientCI;

        uint8 orderType;
        uint256 startTime;
        uint256 endTime;
        bytes32 zoneHash;
        uint256 salt;
        bytes32 conduitKey;
        uint256 counter;

        uint256[] uints;
        require uints[0] == identifierOrCriteriaOI;
        require uints[1] == startAmountOI;
        require uints[2] == endAmountOI;
        require uints[3] == identifierOrCriteriaCI;
        require uints[4] == startAmountCI;
        require uints[5] == endAmountCI;
        require uints[6] == startTime;
        require uints[7] == endTime;
        require uints[8] == salt;
        require uints[9] == counter;

    /* if (f.selector == _validate(((address, address, (uint8, address, uint256, uint256, uint256)[],(uint8, address, uint256, uint256, uint256, address)[], uint8, uint256, uint256, bytes32, uint256, bytes32, uint256), bytes)[]).selector){

    }
    else*/ 
    if (f.selector == _cancel((address, address,( uint8, address, uint256, uint256, uint256)[],(uint8, address, uint256, uint256, uint256, address)[], uint8, uint256, uint256, bytes32, uint256, bytes32, uint256)[]).selector){
        _cancel(e, formOrderComponents(e, 
            offerer,
            zone,

            itemTypeOI,
            tokenOI,
            // identifierOrCriteriaOI,
            // startAmountOI,
            // endAmountOI,

            itemTypeCI,
            tokenCI,
            // identifierOrCriteriaCI,
            // startAmountCI,
            // endAmountCI,
            recipientCI,

            orderType,
            // startTime,
            // endTime,
            zoneHash,
            // salt,
            conduitKey,
            // counter
            uints
        ));
    }
    else {
        calldataarg args;
        f(e, args);
    }
}