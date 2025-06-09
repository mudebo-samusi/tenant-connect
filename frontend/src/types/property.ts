export type PropertyType = 'apartment' | 'house' | 'villa' | 'commercial' | 'land'
export type PropertyStatus = 'available' | 'rented' | 'pending' | 'maintenance'

export interface Property {
  id: number
  title: string
  description?: string
  property_type: PropertyType
  status: PropertyStatus
  address: string
  city: string
  district?: string
  latitude?: number
  longitude?: number
  bedrooms?: number
  bathrooms?: number
  area?: number
  price: number
  currency: string
  is_furnished: boolean
  has_parking: boolean
  has_security: boolean
  has_water: boolean
  has_electricity: boolean
  images?: string[]
  owner_id: number
  created_at: string
  updated_at?: string
}

export interface PropertySearchParams {
  property_type?: PropertyType
  min_price?: number
  max_price?: number
  city?: string
  district?: string
  bedrooms?: number
  bathrooms?: number
  is_furnished?: boolean
  has_parking?: boolean
  has_security?: boolean
  radius?: number
  latitude?: number
  longitude?: number
} 