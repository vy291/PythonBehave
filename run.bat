::run 1 feature ::example --- run Test1_E2E_For_Standard_User --- remove :: on below command
::del listTestCase.txt
::echo features/%1.feature,> listTestCase.txt
::behavex -rf listTestCase.txt --parallel-processes 3
::del listTestCase.txt



::run 1 test suite using tag name ::example --- run @E2E
::behavex --tags="%1" --parallel-processes 3



::run full ::example --- run --- remove :: on below command
behavex --parallel-processes 3



::edit number of parallel-processes if needed --- remove :: on below command
::behavex --parallel-processes 6