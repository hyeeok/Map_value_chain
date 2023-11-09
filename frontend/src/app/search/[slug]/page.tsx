import IndustryInfo from '@/app/search/[slug]/_components/industry-info';

const IndustryInfoPage = ({ params }: { params: { slug: string } }) => {
  return (
    <div>
      <IndustryInfo />
    </div>
  );
};

export default IndustryInfoPage;
