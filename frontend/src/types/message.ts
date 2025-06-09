export interface Message {
  id: number;
  sender_id: number;
  receiver_id: number;
  property_id: number;
  content: string;
  is_read: boolean;
  created_at: string;
}

export interface Conversation {
  user_id: number;
  user_name: string;
  last_message: string;
  last_message_time: string;
  unread_count: number;
  property_id: number;
  property_title: string;
} 