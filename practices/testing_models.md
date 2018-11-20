# Testing Models

There are multiple models of tests, some of which depend on or come after the others.

## Unit tests

Unit tests are tests of specific individual functionality. This test does not take any other part into consideration.

## Integration tests

Integration tests are tests of the integration of multiple components as a whole. This may involve multiple dependencies.

## System tests

System tests are tests to verify an entire system functions as expected. This includes smoke tests, performance tests, regression tests, etc.

## Production tests

These tests verify that live production systems work as expected. If one of these fails, there is a significant unexpected problem which may be customer-facing, which should trigger alerts and potentially trigger a rollback.

## Verification tests

Verification tests, also known as configuration tests, are intended to validate expectations. Instead of verifying if something is working, they simply verify that something looks the way it should. If this test fails, it means something unexpected has occurred, which may need to trigger a redeploy or rollback. Examples of failure would include file corruption, security penetrations, mistakes in configuration, unexpected results of automation processes, etc.

## Stress tests

Stress tests are used to find the limits of a component of a system. They are basically intended to break something, and record what it took to break it, and what the result was.

## Canary test

Canary tests are used to wait a period of time in an attempt to find unexpected problems before continuing a process. On failure, they should immediately revert any changes, and fail whatever process depends on them. Canary tests may use sampling of expected metrics (such as error rates, traffic rates, resource use, load) to trigger a failure when something unexpected occurs.

## Issue-driven tests

Issue-driven tests are tests created from reported issues. As each issue is documented and resolved, a test case is created to check for that issue, so that one will know immediately if it re-occurs.

## Chaos tests

Chaos tests are used to identify unexpected bugs and fix them before they become a larger problem.

