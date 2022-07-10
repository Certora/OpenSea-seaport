import "erc20.spec"

using DummyERC20A as ERC20a
using DummyERC20B as ERC20b
using DummyERC721A as ERC721a
using DummyERC1155A as ERC1155a

methods {
    // envfree methods
    _channels(address) returns(bool) envfree
    _controller() returns(address) envfree
    conduitTransferStructCreator(uint8, address, address, address, uint256, uint256) returns((uint8,address,address,address,uint256,uint256)[]) envfree


    // non-envfree methods
    updateChannel(address, bool)
    execute((uint8, address, address ,address ,uint256 ,uint256)[]) returns(bytes4)
    // execute(uint8, address ,address ,address ,uint256 ,uint256) returns(bytes4)

    safeTransferFrom(address, address, uint256, uint256, bytes) => DISPATCHER(true)
}


function callHelper(method f, env e, address channel, bool isOpen){
    if (f.selector == updateChannel(address, bool).selector) {
        updateChannel(e, channel, isOpen);
	} else {
        calldataarg args;
        f(e, args);
    }
}


rule sanity(method f)
{
	env e;
	calldataarg args;
	f(e,args);
	assert false;
}


// STATUS - verified
// if `updateChannel()` was a successful call, then channel status should change
rule obligedToChange(env e) {
    address channel; 
    bool isOpen;

    bool statusBefore = _channels(channel);

    updateChannel(e, channel, isOpen);

    bool statusAfter = _channels(channel);

    assert statusBefore != statusAfter, "Remember, with great power comes great responsibility.";
}


// STATUS - verified
// nothing else can change `_channels` status except `updateChannel()`. only _controller can change it.
rule whoHowCanChange(env e, method f) {
    address channel; 
    bool isOpen;

    bool statusBefore = _channels(channel);

    calldataarg args;
    f(e, args);

    bool statusAfter = _channels(channel);

    assert statusBefore != statusAfter => f.selector == updateChannel(address, bool).selector && e.msg.sender == _controller(), "Remember, with great power comes great responsibility.";
}


// STATUS - verified
// no changing to a channel status after execution
rule noStateChangeAfterExe(env e, method f) {
    address channel; 
    bool isOpen;

    bool statusBefore = _channels(channel);

    calldataarg args;
    f(e, args);

    bool statusAfter = _channels(channel);

    assert f.selector != updateChannel(address, bool).selector => statusBefore == statusAfter, "Remember, with great power comes great responsibility.";
}


// STATUS - verified
// no executions for closed channels. if all channels are closed, then there is no way to succeed any execution
rule nowhereToRun(env e, method f) filtered {  
                                f -> f.selector == execute((uint8,address,address,address,uint256,uint256)[]).selector 
                                || f.selector == executeWithBatch1155((uint8,address,address,address,uint256,uint256)[],(address,address,address,uint256[],uint256[])[]).selector 
                                || f.selector == executeBatch1155((address,address,address,uint256[],uint256[])[]).selector 
} {
    address channel; 
    bool isOpen;

    require forall address addr. _channels(addr) == false;

    calldataarg args;
    f@withrevert(e, args);

    bool isReverted = lastReverted;

    assert isReverted, "Remember, with great power comes great responsibility.";
}


// STATUS - in progress
// trying to setup environment for executions
rule basicFRule(env e, method f) {
    uint8 itemType;
    address token; address from; address to; address randomUser;
    uint256 identifier; uint256 amount;

    require itemType == 1;
    require token == ERC721a;
    // require randomUser != from && randomUser != to;

    uint256 balanceBefore = ERC20a.balanceOf(e, randomUser);

    // execute(e, conduitTransferStructCreator(itemType, token, from, to, identifier, amount));
    execute(e, itemType, token, from, to, identifier, amount);

    uint256 balanceAfter = ERC20a.balanceOf(e, randomUser);

    assert balanceBefore == balanceAfter, "Remember, with great power comes great responsibility.";
}



