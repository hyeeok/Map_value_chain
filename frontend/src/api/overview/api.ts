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
    return response.data;
  } catch (error) {
    console.log(error);
    throw error;
  }
};

export const getOverviewRelation = async (corpCode: string) => {
  try {
    const response = await apiClient().get(`/overview/${corpCode}/relations`);
    return response.data;
  } catch (error) {
    console.log(error);
  }
};
