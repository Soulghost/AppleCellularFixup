# AppleCellularFixup
Fixup network issues for iPhone in China, based on Siguza's very first 0day.

# Limitation
- iOS < 13.4.5 beta3
- **Not Need to Jailbreak**

# Usage
1. Clone this project.
2. Find the bundle identifier of the app to be repaired.
3. Goto main.m, change the bundle identifier above UIApplicationMain call.
4. Build & Run.

# Reference
1. Based on Siguza's very first 0day - https://twitter.com/s1guza/status/1255641164885131268
2. Thanks for @CodeColorist's sign script - https://gist.github.com/ChiChou/9017580d4adb60d7e43fb9535a8a0273
3. 连个锤子 - http://cydia.saurik.com/package/cn.tinyapps.renet/
