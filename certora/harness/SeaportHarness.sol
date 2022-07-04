pragma solidity >=0.8.13;

// This is the contract that is actually verified; it may contain some helper
// methods for the spec to access internal state, or may override some of the
// more complex methods in the original contract.

// TODO: import the main contract
import "../mungedReference/Seaport.sol";
import { OrderType, BasicOrderType, ItemType, Side } from "../../contracts/lib/ConsiderationEnums.sol";
import {
    OrderComponents,
    BasicOrderParameters,
    OrderParameters,
    Order,
    AdvancedOrder,
    OrderStatus,
    CriteriaResolver,
    Fulfillment,
    FulfillmentComponent,
    Execution,
    OfferItem,
    ConsiderationItem
} from "../../contracts/lib/ConsiderationStructs.sol";
contract SeaportHarness is Seaport {


    Order order_nondet;
    Order order_nondet2;
    //OfferItem[] offerItems_nondet;

    constructor(address conduitController) Seaport(conduitController) {}

	//function fulfillOrder_fields(address offerer,address zone, uint8 itemTypeOferrer,address tokenOfferer,uint256 identifierOrCriteriaOffeer,uint256 startAmountOfferer,uint256 endAmountOfferer,uint8 itemType,address token,uint256 identifierOrCriteria,uint256 startAmount,uint256 endAmount,address payable recipient,uint8 orderType,uint256 startTime,uint256 endTime,bytes32 zoneHash,uint256 salt,bytes32 conduitKey,uint256 totalOriginalConsiderationItems,bytes calldata signature,bytes32 fulfillerConduitKey)
	//function fulfillOrder_fields(address offerer,address zone, uint8 itemTypeOferrer,address tokenOfferer,uint8 itemType,address token,address payable recipient,bytes calldata signature,bytes32 fulfillerConduitKey)
	function fulfillOrder(bytes32 fulfillerConduitKey)
        external
        payable
        notEntered
        //nonReentrant
        returns (bool fulfilled)
    {
        OfferItem memory offerItem1;
        order_nondet2.parameters.offer[0] = offerItem1;

        // OfferItem memory offerItem0 = OfferItem({
        //     itemType:ItemType.ERC1155, 
        //     token:0x001d3F1ef827552Ae1114027BD3ECF1f086bA0F9, 
        //     identifierOrCriteria:0, 
        //     startAmount:0, 
        //     endAmount:0
        //     });

        // require (order_nondet.parameters.offerer == 0x001d3F1ef827552Ae1114027BD3ECF1f086bA0F9);
        // require (order_nondet.parameters.zone == 0x0000000000000000000000000000000000000000);
        // //require (order_nondet.parameters.offer == 0);
        // //require (order_nondet.parameters.consideration == 0);
        // require (order_nondet.parameters.orderType ==  OrderType.FULL_OPEN ); //FULL_OPEN
        // require (order_nondet.parameters.startTime == 0);
        // require (order_nondet.parameters.endTime == 0);
        // require (order_nondet.parameters.zoneHash == 0);
        // require (order_nondet.parameters.salt == 0);
        // require (order_nondet.parameters.conduitKey == 0);
        // require (order_nondet.parameters.totalOriginalConsiderationItems == 8);
        // require (order_nondet.signature == "0");
        // require  (fulfillerConduitKey=="0");


    //       order_nondet.parameters.offerer = 0x001d3F1ef827552Ae1114027BD3ECF1f086bA0F9;
    //     order_nondet.parameters.zone = 0x0000000000000000000000000000000000000000;
    //     //order_nondet.parameters.offer = new OfferItem[](1);
    //    order_nondet.parameters.offer[0] = offerItem0;
    //     //require (order_nondet.parameters.offer.endAmount == offerItems_nondet.endAmount);
        
    //             // //require (order_nondet.parameters.consideration == 0);
    //     order_nondet.parameters.orderType =  OrderType.FULL_OPEN;
    //     order_nondet.parameters.startTime = 0;
    //     order_nondet.parameters.endTime = 0;
    //     order_nondet.parameters.zoneHash = 0;
    //     order_nondet.parameters.salt = 0;
    //     order_nondet.parameters.conduitKey = 0;
    //     order_nondet.parameters.totalOriginalConsiderationItems = 8;
    //     order_nondet.signature = "0";
    //     fulfillerConduitKey="0";

        fulfilled = this.fulfillOrder(order_nondet, fulfillerConduitKey);
       // fulfilled = this.fulfillOrder(order_nondet2, fulfillerConduitKey);
    }

}
//  address offerer; // 0x00
//     address zone; // 0x20
//     OfferItem[] offer; // 0x40
//     ConsiderationItem[] consideration; // 0x60
//     OrderType orderType; // 0x80
//     uint256 startTime; // 0xa0
//     uint256 endTime; // 0xc0
//     bytes32 zoneHash; // 0xe0
//     uint256 salt; // 0x100
//     bytes32 conduitKey; // 0x120
//     uint256 totalOriginalConsiderationItems; 
