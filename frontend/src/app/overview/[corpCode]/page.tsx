import { cookies } from 'next/headers';

import { baseUrl } from '@/api/api-client';
import DescSection from '@/app/overview/[corpCode]/_components/desc-section';
import IndustryInfo from '@/app/overview/[corpCode]/_components/industry-info';
import RelationSection from '@/app/overview/[corpCode]/_components/relation-section';

const getOverviewDesc = async (corpCode: string) => {
  const cookieStore = cookies();
  try {
    const response = await fetch(`${baseUrl}/overview/${corpCode}/description`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.log(error);
  }
};
const getOverviewShareholders = async (corpCode: string) => {
  const cookieStore = cookies();
  try {
    const response = await fetch(
      `${baseUrl}/overview/${corpCode}/shareholders`
    );
    const data = await response.json();
    return data;
  } catch (error) {
    console.log(error);
  }
};

const getOverviewRelation = async (corpCode: string) => {
  const cookieStore = cookies();
  try {
    const response = await fetch(`${baseUrl}/overview/${corpCode}/relations`);
    const data = await response.json();
    return data.data;
  } catch (error) {
    console.log(error);
  }
};

const IndustryInfoPage = async ({
  params,
}: {
  params: { corpCode: string };
}) => {
  const overviewDescData = await getOverviewDesc(params.corpCode);
  const overviewShareholders = await getOverviewShareholders(params.corpCode);
  const overviewRelationData = await getOverviewRelation(params.corpCode);

  return (
    <div className="flex flex-col gap-6">
      <DescSection
        data={overviewDescData}
        shareholderData={overviewShareholders}
      />
      {overviewRelationData.length > 0 && (
        <RelationSection
          data={overviewRelationData}
          corpCode={params.corpCode}
        />
      )}
      <IndustryInfo />
    </div>
  );
};

export default IndustryInfoPage;
