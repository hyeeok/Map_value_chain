import {
  DialogContent,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog';
import {
  Table,
  TableBody,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';

export interface DescDialogType {
  title: string;
  headDataList: string[];
  children: React.ReactNode;
  size?: string;
}
const DescDialog = ({
  title,
  headDataList,
  children,
  size,
}: DescDialogType) => {
  const maxWidthClass = size === 'large' ? `max-w-[68rem]` : '';

  return (
    <DialogContent className={maxWidthClass}>
      <DialogHeader>
        <DialogTitle>{title}</DialogTitle>
      </DialogHeader>
      <div className="max-h-[420px] overflow-y-auto">
        <Table>
          <TableHeader>
            <TableRow>
              {headDataList.map((headData, hi) => (
                <TableHead key={hi}>{headData}</TableHead>
              ))}
            </TableRow>
          </TableHeader>
          <TableBody>{children}</TableBody>
        </Table>
      </div>
    </DialogContent>
  );
};

export default DescDialog;
