import "erc20.spec"


methods {
    _getFraction(uint256, uint256, uint256) returns(uint256) => NONDET
}


// rule sanity(method f)
// {
// 	env e;
// 	calldataarg args;
// 	f(e,args);
// 	assert false;
// }


rule whoChangedOrder(method f, address u) filtered { f -> f.selector == fulfillOrder(((address,address,(uint8,address,uint256,uint256,uint256)[],(uint8,address,uint256,uint256,uint256,address)[],uint8,uint256,uint256,bytes32,uint256,bytes32,uint256),bytes),bytes32).selector } {
    env eB;
    env eF;
	calldataarg args;
	bytes32 orderHash;
	bool isValidatedBefore; bool isCancelledBefore;
    uint256 totalFilledBefore; uint256 totalSizeBefore; 
    
    address offerer;
    uint256 counterBefore;

    isValidatedBefore,isCancelledBefore,totalFilledBefore,totalSizeBefore = getOrderStatus(eB, orderHash);
    counterBefore = getCounter(eB, offerer);

    f(eF,args);

	bool isValidatedAfter; bool isCancelledAfter;
    uint256 totalFilledAfter; uint256 totalSizeAfter;

    uint256 counterAfter;

    isValidatedAfter,isCancelledAfter,totalFilledAfter,totalSizeAfter = getOrderStatus(eB, orderHash);
    counterAfter = getCounter(eB, offerer);

    assert isValidatedAfter == isValidatedBefore;
    assert isCancelledAfter == isCancelledBefore;
    assert totalFilledAfter == totalFilledBefore;
    assert totalSizeAfter == totalSizeBefore;
    assert counterBefore == counterAfter;
}

rule basicFRule(env e, method f) {

    // declare variables / write requirements

    calldataarg args;
    f(e, args);

    // declare variables / write requirements / more asserts to the God of asserts

    assert false, "Remember, with great power comes great responsibility.";
}

ghost ghostName(uint256) returns uint256;

ghost ghostName(uint256) returns uint256 {
    init_state axiom forall uint256 a. ghostName(a) == 0;
}   

hook Sstore contactsMap[KEY uint256 defaultName] uint256 defaultValue
    (uint256 old_defaultValue) STORAGE
{
    havoc ghostName assuming forall uint256 a. a == defaultName => ghostName@new(a) == ghostName@old(a) + defaultValue - old_defaultValue
        && a == defaultName => ghostName@new(a) == ghostName@old(a)
}
