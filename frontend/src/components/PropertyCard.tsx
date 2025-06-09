import Image from 'next/image'
import Link from 'next/link'
import { Property } from '@/types/property'

interface PropertyCardProps {
  property: Property
}

export default function PropertyCard({ property }: PropertyCardProps) {
  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden">
      <div className="relative h-48">
        <Image
          src={property.images?.[0] || '/placeholder-property.jpg'}
          alt={property.title}
          fill
          className="object-cover"
        />
        <div className="absolute top-2 right-2 bg-indigo-600 text-white px-2 py-1 rounded text-sm">
          {property.property_type}
        </div>
      </div>
      
      <div className="p-4">
        <Link href={`/properties/${property.id}`}>
          <h3 className="text-lg font-semibold text-gray-900 hover:text-indigo-600">
            {property.title}
          </h3>
        </Link>
        
        <p className="mt-1 text-sm text-gray-500">
          {property.address}, {property.city}
        </p>
        
        <div className="mt-2 flex items-center text-sm text-gray-500">
          {property.bedrooms && (
            <span className="flex items-center mr-4">
              <svg className="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
              </svg>
              {property.bedrooms} beds
            </span>
          )}
          {property.bathrooms && (
            <span className="flex items-center mr-4">
              <svg className="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
              {property.bathrooms} baths
            </span>
          )}
          {property.area && (
            <span className="flex items-center">
              <svg className="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4" />
              </svg>
              {property.area}m²
            </span>
          )}
        </div>
        
        <div className="mt-4 flex items-center justify-between">
          <div className="text-lg font-semibold text-gray-900">
            {new Intl.NumberFormat('en-UG', {
              style: 'currency',
              currency: property.currency
            }).format(property.price)}
            <span className="text-sm text-gray-500">/month</span>
          </div>
          
          <div className="flex space-x-2">
            {property.is_furnished && (
              <span className="inline-flex items-center px-2 py-1 rounded text-xs font-medium bg-green-100 text-green-800">
                Furnished
              </span>
            )}
            {property.has_parking && (
              <span className="inline-flex items-center px-2 py-1 rounded text-xs font-medium bg-blue-100 text-blue-800">
                Parking
              </span>
            )}
          </div>
        </div>
      </div>
    </div>
  )
} 