export type VCMapElementType = {
  domainCode: string;
  domainName: string;
  domainDivision: string;
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
        <div
          key={di}
          className={`flex flex-col px-6 py-4 flex-auto box-border ${
            divisionColor[domainItem.domainDivision]
          }`}
        >
          <div>
            <div className="inline-block flex justify-between text-primary-foreground">
              {domainItem.domainName}
            </div>
          </div>
          <div>
            <div>
              <label className="text-xs font-medium leading-none mb-2 text-primary-foreground">
                Classes
              </label>
              <div className="flex flex-wrap gap-2">
                {domainItem.classList.map((classItem, ci) => (
                  <div
                    key={ci}
                    className="px-2.5 py-1.5 border text-xs text-primary-foreground"
                  >
                    {classItem.industryClassName}
                  </div>
                ))}
              </div>
            </div>
            <div>
              <label className="text-xs font-medium leading-none mb-2 text-primary-foreground">
                Themes
              </label>
              <div className="flex flex-wrap gap-2">
                {domainItem.themeList.map((themeItem, ti) => (
                  <div
                    key={ti}
                    className="px-2 py-1 border text-xs text-primary-foreground"
                  >
                    {themeItem.industryClassName}
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default VCMap;
