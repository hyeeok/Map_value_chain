import { ChevronLeft, ChevronRight } from 'lucide-react';

import { Button } from '@/components/ui/button';

const Pagination = ({
  handlePageClick,
  currentPage,
  pageNum,
}: {
  handlePageClick: (targetPage: number) => void;
  currentPage: number;
  pageNum: number;
}) => {
  const numArray = Array.from({ length: pageNum }).map((v, i) => i + 1);
  return (
    <>
      <Button variant="link" size="sm" disabled={currentPage <= 1}>
        <ChevronLeft className="w-4 h-4" />
      </Button>
      {numArray.map((i) => (
        <Button
          variant="link"
          size="sm"
          key={i}
          onClick={() => handlePageClick(i)}
          className={`${
            currentPage === i ? 'bg-primary text-primary-foreground' : ''
          }`}
        >
          {i}
        </Button>
      ))}
      <Button variant="link" size="sm" disabled={currentPage >= pageNum}>
        <ChevronRight className="w-4 h-4" />
      </Button>
    </>
  );
};

export default Pagination;
