import React from 'react';
import { UserProfile } from '@/types/user';

interface ProfileViewProps {
  profile: UserProfile;
  onEdit: () => void;
}

export default function ProfileView({ profile, onEdit }: ProfileViewProps) {
  return (
    <div className="space-y-4">
      <div>
        <h2 className="text-sm font-medium text-gray-700">Phone Number</h2>
        <p className="mt-1">{profile.phone_number}</p>
      </div>
      {profile.bio && (
        <div>
          <h2 className="text-sm font-medium text-gray-700">Bio</h2>
          <p className="mt-1">{profile.bio}</p>
        </div>
      )}
      <div>
        <h2 className="text-sm font-medium text-gray-700">Account Type</h2>
        <p className="mt-1 capitalize">{profile.user_type}</p>
      </div>
      <button
        onClick={onEdit}
        className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
      >
        Edit Profile
      </button>
    </div>
  );
} 