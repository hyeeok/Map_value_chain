import { apiClient } from '@/api/api-client';

export const getOverviewhList = async ({
  category,
  keyword,
  limit,
  page,
}: {
  category?: string | null;
  keyword?: string | null;
  limit?: string | number | null;
  page?: string | number | null;
}) => {
  try {
    const response = await apiClient().get(`/overview`, {
      params: {
        // ...(option && { option: option }),
        category,
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
