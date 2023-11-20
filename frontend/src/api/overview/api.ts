import { apiClient } from '@/api/api-client';

export const getOverviewhList = async (
  option: string = 'corpName',
  keyword: string = '',
  limit: number = 20,
  page: number = 1
) => {
  try {
    const response = await apiClient().get(`/overview`, {
      params: {
        // ...(option && { option: option }),
        option,
        keyword,
        limit,
        page,
      },
    });
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.log(error);
    throw error;
  }
};
