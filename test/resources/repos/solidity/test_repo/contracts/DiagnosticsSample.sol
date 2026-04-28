pragma solidity ^0.8.0;

contract DiagnosticsSample {
    function brokenFactory() public pure returns (string memory) {
        return missingGreeting;
    }
}
