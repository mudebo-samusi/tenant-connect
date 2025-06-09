import React from 'react';
import { UserProfile } from '@/types/user';

interface ProfileHeaderProps {
  profile: UserProfile;
}

export default function ProfileHeader({ profile }: ProfileHeaderProps) {
  return (
    <div className="mb-6">
      <h1 className="text-2xl font-bold">{profile.full_name}</h1>
      <p className="text-gray-600">{profile.email}</p>
      {profile.is_verified && (
        <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800 mt-2">
          Verified
        </span>
      )}
    </div>
  );
} 