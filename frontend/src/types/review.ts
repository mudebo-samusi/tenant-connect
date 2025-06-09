export interface Review {
  id: number;
  property_id: number;
  reviewer_id: number;
  reviewer_name: string;
  rating: number;
  comment: string;
  created_at: string;
  updated_at: string | null;
} 