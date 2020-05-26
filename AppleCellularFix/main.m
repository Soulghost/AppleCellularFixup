//
//  main.m
//  AppleCellularFix
//
//  Created by soulghost on 2020/5/26.
//  Copyright © 2020 soulghost. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "AppDelegate.h"
#import "SGNetworkConfigurationModifier.h"

int main(int argc, char * argv[]) {
    NSString * appDelegateClassName;
    @autoreleasepool {
        // Setup code that might create autoreleased objects goes here.
        appDelegateClassName = NSStringFromClass([AppDelegate class]);
    }
    
    // do fix
    [SGNetworkConfigurationModifier resolveNetworkProblmeForAppWithBundleId:@"com.taobao.taobao4iphone"];
    return UIApplicationMain(argc, argv, nil, appDelegateClassName);
}
