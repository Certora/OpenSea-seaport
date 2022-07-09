// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "../mungedReference/lib/ReferenceOrderValidator.sol";

import { ItemType } from "../mungedAssembly/lib/ConsiderationEnums.sol";
import { OfferItem, ConsiderationItem } from "certora/mungedAssembly/lib/ConsiderationStructs.sol";

contract ReferenceOrderValidatorHarness is ReferenceOrderValidator {


    constructor(address conduitController)
        ReferenceOrderValidator(conduitController)
    {}

    function getOrderNum(bytes32 orderHash)
        public
        view
        returns (uint256)
    {
        uint256 numenator;
        ( , , numenator, ) = _getOrderStatus(orderHash);
        return numenator;
    }

    function getOrderDenum(bytes32 orderHash)
        public
        view
        returns (uint256)
    {
        uint256 denominator;
        ( , , , denominator) = _getOrderStatus(orderHash);
        return denominator;
    }

    function isOrderValid(bytes32 orderHash)
        public
        view
        returns (bool)
    {
        bool isValidated;
        (isValidated , , ,) = _getOrderStatus(orderHash);
        return isValidated;
    }

    function isOrderCancelled(bytes32 orderHash)
        public
        view
        returns (bool)
    {
        bool isCancelled;
        ( , isCancelled, ,) = _getOrderStatus(orderHash);
        return isCancelled;
    }

    function formOrderComponents(
        address offerer,
        address zone,

        ItemType itemTypeOI,
        address tokenOI,
        uint256 identifierOrCriteriaOI,
        uint256 startAmountOI,
        uint256 endAmountOI,

        ItemType itemTypeCI,
        address tokenCI,
        uint256 identifierOrCriteriaCI,
        uint256 startAmountCI,
        uint256 endAmountCI,
        address recipientCI,

        OrderType orderType,
        uint256 startTime,
        uint256 endTime,
        bytes32 zoneHash,
        uint256 salt,
        bytes32 conduitKey,
        uint256 counter
    ) public returns (OrderComponents[] memory orders) {
        // OfferItem[] offer = new OfferItem[](1);
        // offer[0] = OfferItem(
        //     itemTypeOI,
        //     tokenOI,
        //     identifierOrCriteriaOI,
        //     startAmountOI,
        //     endAmountOI
        // );

        // ConsiderationItem[] consideration = new ConsiderationItem[](1);
        // consideration[0] = ConsiderationItem(
        //     itemTypeCI,
        //     tokenCI,
        //     identifierOrCriteriaCI,
        //     startAmountCI,
        //     endAmountCI,
        //     recipientCI
        // );

        orders = new OrderComponents[](1);
        orders[0] = OrderComponents(
            offerer,
            zone,
            OfferItem(
                itemTypeOI,
                tokenOI,
                identifierOrCriteriaOI,
                startAmountOI,
                endAmountOI
            ),
            ConsiderationItem(
                itemTypeCI,
                tokenCI,
                identifierOrCriteriaCI,
                startAmountCI,
                endAmountCI,
                recipientCI
            ),
            orderType,
            startTime,
            endTime,
            zoneHash,
            salt,
            conduitKey,
            counter
        );
    }

}
