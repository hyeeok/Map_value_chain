import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';

export type VCMapElementType = {
  domainCode: string;
  domainName: string;
  domainDivision: number;
  classList: {
    industryClassCode: string;
    industryClassName: string;
    industryClassType: string;
  }[];
  themeList: {
    industryClassCode: string;
    industryClassName: string;
    industryClassType: string;
  }[];
};

const divisionColor = {
  '1': 'bg-zinc-700',
  '2': 'bg-blue-900',
  '3': 'bg-green-800',
  '4': 'bg-pink-900',
  '5': 'bg-yellow-600',
};

const VCMap = ({ data }: { data: VCMapElementType[] }) => {
  return (
    <div className="flex flex-wrap gap-2">
      {data.map((domainItem, di) => (
        <Card
          key={di}
          className={`flex-auto box-border ${
            divisionColor[domainItem.domainDivision]
          }`}
        >
          <CardHeader>
            <CardTitle className="inline-block flex justify-between text-primary-foreground">
              {domainItem.domainName}
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div>
              <label className="text-sm font-medium leading-none mb-2 text-primary-foreground">
                Classes
              </label>
              <div className="flex flex-wrap gap-2">
                {domainItem.classList.map((classItem, ci) => (
                  <div
                    key={ci}
                    className="px-4 py-2 border text-sm text-primary-foreground"
                  >
                    {classItem.industryClassName}
                  </div>
                ))}
              </div>
            </div>
            <div className="pt-2">
              <label className="text-sm font-medium leading-none mb-2 text-primary-foreground">
                Themes
              </label>
              <div className="flex flex-wrap gap-2">
                {domainItem.themeList.map((themeItem, ti) => (
                  <div
                    key={ti}
                    className="px-4 py-2 border text-sm text-primary-foreground"
                  >
                    {themeItem.industryClassName}
                  </div>
                ))}
              </div>
            </div>
          </CardContent>
        </Card>
      ))}
    </div>
  );
};

export default VCMap;
