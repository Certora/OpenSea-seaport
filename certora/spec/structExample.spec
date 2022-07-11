import "erc20.spec"
val importedStructs: Map<ReferenceVerifiers, OrderStatus>

methods {
    _getFraction(uint256, uint256, uint256) returns(uint256) => NONDET
}
OrderStatus orderStatus;

rule revertOnInvalidCheck (bytes32 orderHash, bool onlyAllowUnused, bool revertOnInvalid){
// rule revertOnInvalidCheck (){
// OrderStatus orderStatus;
bool valid;
valid = _verifyOrderStatus(orderHash, orderStatus, onlyAllowUnused, revertOnInvalid);

assert(revertOnInvalid => valid,"if revertOnInvalid is true then function must only revert if order is not verified");

}



// rule sanity(method f)
// {
// 	env e;
// 	calldataarg args;
// 	f(e,args);
// 	assert false;
// }


// rule whoChangedOrder(method f, address u) filtered { f -> f.selector == fulfillOrder(((address,address,(uint8,address,uint256,uint256,uint256)[],(uint8,address,uint256,uint256,uint256,address)[],uint8,uint256,uint256,bytes32,uint256,bytes32,uint256),bytes),bytes32).selector } {
//     env eB;
//     env eF;
// 	calldataarg args;
// 	bytes32 orderHash;
// 	bool isValidatedBefore; bool isCancelledBefore;
//     uint256 totalFilledBefore; uint256 totalSizeBefore; 
    
//     address offerer;
//     uint256 counterBefore;

//     isValidatedBefore,isCancelledBefore,totalFilledBefore,totalSizeBefore = getOrderStatus(eB, orderHash);
//     counterBefore = getCounter(eB, offerer);

//     f(eF,args);

// 	bool isValidatedAfter; bool isCancelledAfter;
//     uint256 totalFilledAfter; uint256 totalSizeAfter;

//     uint256 counterAfter;

//     isValidatedAfter,isCancelledAfter,totalFilledAfter,totalSizeAfter = getOrderStatus(eB, orderHash);
//     counterAfter = getCounter(eB, offerer);

//     assert isValidatedAfter == isValidatedBefore;
//     assert isCancelledAfter == isCancelledBefore;
//     assert totalFilledAfter == totalFilledBefore;
//     assert totalSizeAfter == totalSizeBefore;
//     assert counterBefore == counterAfter;
// }
