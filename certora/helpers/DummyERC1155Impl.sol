pragma solidity ^0.8.0;

import "./SafeMath.sol";

/*
    A very incomplete implementation of ERC1155 that only foscuses on transferFrom and ownership tracking.
    Lacks support for approvals, "safe checks" on recipients, and some other sensible checks.
    Meant to be used as a stab; Expand it in a different contract if needed.
*/
contract DummyERC1155Impl {
    using SafeMath for uint256;

    string public name;
    string public symbol;

    // Mapping from token ID to account balances
    mapping(uint256 => mapping(address => uint256)) private _balances;

    // Mapping from account to operator approvals
    // mapping(address => mapping(address => bool)) private _operatorApprovals;
    
    function balanceOf(address owner, uint256 tokenId) external view returns (uint256) {
        require(owner != address(0), "ERC1155: Zero Address is invalid");
        return _balances[tokenId][owner];
    }

    //Not so Safe transfers
    function safeTransferFrom(
        address from,
        address to,
        uint256 id,
        uint256 amount,
        bytes calldata data
    ) external {
        require(to != address(0));

        // No approval checks

        _transferFrom(from, to, id, amount);

        // DOES NOT VERIFY
    }

    function safeBatchTransferFrom(
        address from,
        address to,
        uint256[] calldata ids,
        uint256[] calldata amounts,
        bytes calldata data
    ) external {
        require(to != address(0));

        // No approval checks

        for (uint256 i = 0; i < ids.length; i++) {
            _transferFrom(from, to, ids[i], amounts[i]);            
        }

        // DOES NOT VERIFY
    }

    function _transferFrom(address from, address to, uint256 id, uint256 amount) private {
        _balances[id][from] = _balances[id][from].sub(amount);
        _balances[id][to] = _balances[id][to].add(amount);
    }
}