*** Variables ***

${BROWSER}              chrome
${FRONTEND_URL}         http://localhost:4300


*** Settings ***

Documentation   JwtLibrary Acceptance Tests

Library         SeleniumLibrary  timeout=10  implicit_wait=0
Library         JwtLibrary
Library         DebugLibrary

Test Setup      Test Setup
Test Teardown   Test Teardown


*** Test Cases ***

Scenario: Test JwtLibrary
  # Go To  ${FRONTEND_URL}
  # Wait until page contains  Plone
  ${token}=  Enable JWT autologin as
  Log  ${token}  WARN
  Add cookie  auth_token  ${token}
  Wait until page contains  Plone
  Reload page
  Wait until element is visible  css=.left.fixed.menu
  Page should contain  Log out


*** Keywords ***

Test Setup
  Open Browser  ${FRONTEND_URL}  ${BROWSER}
  Set Window Size  1280  1024

Test Teardown
  Close Browser
