// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "../mungedReference/conduit/ReferenceConduit.sol";

contract ReferenceConduitHarness is ReferenceConduit {


    constructor() ReferenceConduit() { }


    function conduitTransferStructCreator(
        ConduitItemType itemType, 
        address token, 
        address from, 
        address to, 
        uint256 identifier, 
        uint256 amount
    ) public returns (ConduitTransfer[] memory transfers) {
        transfers = new ConduitTransfer[](1);
        transfers[0] = ConduitTransfer(
            itemType,
            token,
            from,
            to,
            identifier,
            amount
        );
    }

    function execute(
        ConduitItemType itemType, 
        address token, 
        address from, 
        address to, 
        uint256 identifier, 
        uint256 amount
    )
        public                                                  // HARNESS: external -> public
        returns (bytes4 magicValue)
    {
        return super.execute(conduitTransferStructCreator(itemType, token, from, to, identifier, amount));
    }

}
