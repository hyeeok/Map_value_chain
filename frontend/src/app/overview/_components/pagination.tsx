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
  const startPageNum = currentPage - 1 - ((currentPage - 1) % 10) + 1;
  const endPageNum = currentPage - 1 - ((currentPage - 1) % 10) + 10;

  const numArray = Array.from(
    { length: endPageNum - startPageNum + 1 },
    (_, i) => startPageNum + i
  );

  return (
    <>
      <Button
        variant="link"
        size="sm"
        onClick={() => handlePageClick(currentPage - 1)}
        disabled={currentPage <= 1}
      >
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
      <Button
        variant="link"
        size="sm"
        onClick={() => handlePageClick(currentPage + 1)}
        disabled={currentPage >= pageNum}
      >
        <ChevronRight className="w-4 h-4" />
      </Button>
    </>
  );
};

export default Pagination;
