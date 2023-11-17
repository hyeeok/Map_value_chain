'use client';

import Link from 'next/link';
import React from 'react';

import {
  ListItem,
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  navigationMenuTriggerStyle,
} from '@/components/ui/navigation-menu';
import { cn } from '@/lib/utils';

const Header = () => {
  return (
    <header
      className="
      border-b sticky top-0 z-50
      bg-background/95 backdrop-blur
      supports-[backdrop-filter]:bg-background/60
      "
    >
      <div className="container flex gap-4 items-center h-14">
        <div>
          <Link href="/">
            <span className="font-bold">MVC</span>
          </Link>
        </div>
        <NavigationMenu>
          <NavigationMenuList className="gap-2">
            <NavigationMenuItem>
              <Link href="/flowmap" legacyBehavior passHref>
                <NavigationMenuLink
                  className={
                    (cn(navigationMenuTriggerStyle()), 'bg-transparent')
                  }
                >
                  Value Chain Map
                </NavigationMenuLink>
              </Link>
            </NavigationMenuItem>
            <NavigationMenuItem>
              <Link href="/overview" legacyBehavior passHref>
                <NavigationMenuLink
                  className={
                    (cn(navigationMenuTriggerStyle()), 'bg-transparent')
                  }
                >
                  기업개황
                </NavigationMenuLink>
              </Link>
            </NavigationMenuItem>
            <NavigationMenuItem>
              <NavigationMenuTrigger
                className={(cn(navigationMenuTriggerStyle()), 'bg-transparent')}
              >
                Item One
              </NavigationMenuTrigger>
              <NavigationMenuContent>
                <ul className="grid grid-cols-2 gap-3 p-4 md:w-[400px] lg:w-[500px] ">
                  <ListItem>description</ListItem>
                </ul>
              </NavigationMenuContent>
            </NavigationMenuItem>
          </NavigationMenuList>
        </NavigationMenu>
      </div>
    </header>
  );
};

export default Header;
