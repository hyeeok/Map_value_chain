// import { cookies } from 'next/headers';
import React from 'react';

// import { baseUrl } from '@/api/api-client';
import OverviewList from '@/app/overview/_components/overview-list';
// import { OVERVIEW_RESPONSE } from '@/app/overview/_test/overview';

// const getOverviewList = async () => {
//   const cookieStore = cookies();
//   try {
//     const response = await fetch(`${baseUrl}/overview`);
//     const data = await response.json();
//     return data;
//   } catch (error) {
//     console.log(error);
//   }
// };

const OverviewPage = async () => {
  // const overviewListData = await getOverviewList();
  // const overviewListData = OVERVIEW_RESPONSE;

  return (
    <div>
      <OverviewList />
    </div>
  );
};

export default OverviewPage;
