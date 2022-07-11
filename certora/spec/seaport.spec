import "erc20.spec"
// val importedStructs: Map<ReferenceVerifiers, OrderStatus>
using ReferenceVerifiers as rv
// methods {
//     _getFraction(uint256, uint256, uint256) returns(uint256) => NONDET
// }


definition Unfilled(uint256 num) returns bool = num == 0;
definition PartiallyFilled(uint256 num, uint256 den) returns bool =
num != 0 && num < den;



// _verifyTime function 
    // This function should revert only when the current block time is outside the start and end time, and the revertOnInvalid argument is true

rule revertOnlyOnInvalidAndRevertFlag(env e, uint256 startTime, uint256 endTime, bool revertOnInvalid){
    require e.msg.value == 0;
    _verifyTime@withrevert(e, startTime, endTime, revertOnInvalid);
    assert lastReverted <=> (e.block.timestamp < startTime || e.block.timestamp >= endTime) && revertOnInvalid,"function can revert only when revertOnInvalid flag is true and order is currently inactive";
}
 
    //Function must return true if the block time is within the start and end time range 
rule returnTrueIfTimeValid(env e, uint256 startTime, uint256 endTime, bool revertOnInvalid){
    require e.msg.value == 0;
    bool valid = _verifyTime@withrevert(e, startTime, endTime, revertOnInvalid);
    assert (e.block.timestamp >= startTime && e.block.timestamp < endTime) => valid,"function must return true if block time is within the start and end time range";
}

    //Function can return false only if the block time is not in the start and end time range and revertOnInvalid is false 
rule returnFalseIfTimeValidAndrevertOnInvalidFalse(env e, uint256 startTime, uint256 endTime, bool revertOnInvalid){
    require e.msg.value == 0;
    bool valid = _verifyTime(e, startTime, endTime, revertOnInvalid);
    assert !valid <=> (e.block.timestamp < startTime || e.block.timestamp >= endTime) && !revertOnInvalid,"function can return false if and only if the block time is outside the start and end time range and revertOnInvalid is false";
}



// _verifyOrderStatus function


rule returnTrueIfOrderValid(env e, bytes32 orderHash, rv.OrderStatus orderStatus, bool onlyAllowUnused, bool revertOnInvalid){

    bool valid = _verifyOrderStatus(e, orderHash, orderStatus, onlyAllowUnused, revertOnInvalid);

    assert !orderStatus.isCancelled && 
    (Unfilled(orderStatus.numerator) || (PartiallyFilled(orderStatus.numerator, orderStatus.denominator) && !onlyAllowUnused)) 
    <=> valid,
    "function must return true if order is not cancelled and either unfilled or partilly filled with onlyAllowUnused being false";

}

rule invalidOrderRevertCheck(env e, bytes32 orderHash, rv.OrderStatus orderStatus, bool onlyAllowUnused, bool revertOnInvalid){
    require e.msg.value == 0;

    bool valid = _verifyOrderStatus@withrevert(e, orderHash, orderStatus, onlyAllowUnused, revertOnInvalid);
    
    assert lastReverted <=> !(!orderStatus.isCancelled && 
                            (Unfilled(orderStatus.numerator) || (PartiallyFilled(orderStatus.numerator, orderStatus.denominator) && !onlyAllowUnused))) &&
                            revertOnInvalid
                            ,"function must revert iff the order is invalid and revertOnInvalid is true";
}


rule invalidOrderReturnCheck(env e, bytes32 orderHash, rv.OrderStatus orderStatus, bool onlyAllowUnused, bool revertOnInvalid){
    require e.msg.value == 0;

    bool valid = _verifyOrderStatus(e, orderHash, orderStatus, onlyAllowUnused, revertOnInvalid);
    
    assert !valid <=> !(!orderStatus.isCancelled && 
                            (Unfilled(orderStatus.numerator) || (PartiallyFilled(orderStatus.numerator, orderStatus.denominator) && !onlyAllowUnused)))
                            ,"function must return false iff the order is invalid and revertOnInvalid is false";
}


rule revertOnInvalidCheck (env e, bytes32 orderHash, rv.OrderStatus orderStatus, bool onlyAllowUnused, bool revertOnInvalid){

// require revertOnInvalid;

bool valid = _verifyOrderStatus(e, orderHash, orderStatus, onlyAllowUnused, revertOnInvalid);

assert(revertOnInvalid => valid,"if revertOnInvalid is true then function must only revert if order is not verified");
// assert(valid,"if revertOnInvalid is true then function must only revert if order is not verified");
// assert false;
}

rule invalidIfOrderCancelled (env e, bytes32 orderHash, rv.OrderStatus orderStatus, bool onlyAllowUnused, bool revertOnInvalid){

// require !revertOnInvalid && orderStatus.isCancelled;
bool valid = _verifyOrderStatus(e, orderHash, orderStatus, onlyAllowUnused, revertOnInvalid);

assert(!revertOnInvalid && orderStatus.isCancelled => !valid,"if order status is cancelled then it cannot be verified");
// assert false;
}



rule invalidOrderIfInvalidFraction (env e, bytes32 orderHash, rv.OrderStatus orderStatus, bool onlyAllowUnused, bool revertOnInvalid){

uint256 nemeratorBefore = orderStatus.numerator;
uint256 denominatorBefore = orderStatus.denominator;
// require !revertOnInvalid && orderStatus.numerator >= orderStatus.denominator && orderStatus.numerator !=0;
bool valid = _verifyOrderStatus(e, orderHash, orderStatus, onlyAllowUnused, revertOnInvalid);

assert(!revertOnInvalid && orderStatus.numerator >= orderStatus.denominator && orderStatus.numerator !=0 => !valid,"if order is already filled then it cannot be verified");
// assert false;
}

rule ivalidUsedOrderIfUnusedOrderRequired(env e, bytes32 orderHash, rv.OrderStatus orderStatus, bool onlyAllowUnused, bool revertOnInvalid){

// require !revertOnInvalid && onlyAllowUnused && orderStatus.numerator!=0;
bool valid = _verifyOrderStatus(e, orderHash, orderStatus, onlyAllowUnused, revertOnInvalid);

assert(!revertOnInvalid && onlyAllowUnused && orderStatus.numerator!=0 => !valid,"if unused order required then used orders cannot be verified");
// assert false;

}


rule revertOnInvalidTimeCheck (env e, uint256 startTime, uint256 endTime, bool revertOnInvalid){

require startTime>e.block.timestamp;
bool validBefore;
validBefore = _verifyTime@withrevert(e, startTime, endTime, revertOnInvalid);
bool validAfter = validBefore;

assert(revertOnInvalid => validAfter,"if revertOnInvalid is true then function must only revert if time is not verified");
// assert(valid,"if revertOnInvalid is true then function must only revert if order is not verified");
// assert false;
}

rule ivalidOrderIfOutsideStartEndTime(env e, uint256 startTime, uint256 endTime, bool revertOnInvalid){

// require !revertOnInvalid && onlyAllowUnused && orderStatus.numerator!=0;
bool valid = _verifyTime(e, startTime, endTime, revertOnInvalid);

assert(valid => e.block.timestamp >= startTime && e.block.timestamp <= endTime,"if unused order required then used orders cannot be verified");
// assert false;

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
