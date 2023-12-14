// import { cookies } from 'next/headers';
import React from 'react';

// import { baseUrl } from '@/api/api-client';
// import OverviewList from '@/app/overview/_components/overview-list';

// const getOverview = async () => {
//   const cookieStore = cookies();
//   try {
//     const response = await fetch(`${baseUrl}/overview?limit=20`);
//     const data = await response.json();
//     return data;
//   } catch (error) {
//     console.log(error);
//   }
// };

const OverviewPage = async () => {
  // const OverviewListData = await getOverview();
  return (
    <>
      <div>검색어를 입력하세요</div>
      {/* <OverviewList data={OverviewListData} /> */}
    </>
  );
};

export default OverviewPage;
