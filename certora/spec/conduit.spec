import "erc20.spec"

methods {
    // envfree methods
    _channels(address) returns(bool) envfree
    _controller() returns(address) envfree


    // non-envfree methods
    updateChannel(address, bool)

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
