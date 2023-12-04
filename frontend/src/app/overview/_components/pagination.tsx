import {
  ChevronLeft,
  ChevronRight,
  ChevronsLeft,
  ChevronsRight,
} from 'lucide-react';

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
  const startPageNum = Math.floor((currentPage - 1) / 10) * 10 + 1;
  const endPageNum = Math.min(
    (Math.floor((currentPage - 1) / 10) + 1) * 10,
    pageNum
  );

  const numArray = Array.from(
    { length: endPageNum - startPageNum + 1 },
    (_, i) => startPageNum + i
  );

  return (
    <div className="flex justify-center">
      <Button
        variant="link"
        size="sm"
        onClick={() => handlePageClick(1)}
        disabled={currentPage === 1}
      >
        <ChevronsLeft className="w-4 h-4" />
      </Button>
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
      <Button
        variant="link"
        size="sm"
        onClick={() => handlePageClick(pageNum)}
        disabled={currentPage == pageNum}
      >
        <ChevronsRight className="w-4 h-4" />
      </Button>
    </div>
  );
};

export default Pagination;
