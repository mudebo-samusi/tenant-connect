export interface UserProfile {
  id: number;
  email: string;
  full_name: string;
  phone_number: string;
  profile_picture: string | null;
  bio: string | null;
  user_type: string;
  is_verified: boolean;
  created_at: string;
  updated_at: string | null;
}

export interface UserUpdate {
  full_name?: string;
  phone_number?: string;
  bio?: string;
  profile_picture?: string;
} 