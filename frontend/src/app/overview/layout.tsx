import { cookies } from 'next/headers';
import React from 'react';

import { baseUrl } from '@/api/api-client';
import Sidenav from '@/app/overview/_components/sidenav';
import { buildHierarchy } from '@/app/overview/_lib/sidenav-lib';
import { SIDENAV_DATA } from '@/app/overview/_test/sidenav';

const getOverviewIndex = async () => {
  const cookieStore = cookies();
  try {
    const response = await fetch(`${baseUrl}/overview/index`);
    const responseJson = await response.json();
    const data = buildHierarchy(responseJson);
    return data;
  } catch (error) {
    console.log(error);
  }
};

const OverviewLayout = async ({ children }: { children: React.ReactNode }) => {
  const sidenavData =
    (await getOverviewIndex()) || buildHierarchy(SIDENAV_DATA.data);

  return (
    <div className="container flex flex-col px-8">
      <section className="flex flex-1 gap-6">
        <Sidenav sidenav={sidenavData} />
        {children}
      </section>
    </div>
  );
};

export default OverviewLayout;
