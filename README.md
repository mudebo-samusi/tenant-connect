# TenantConnect

A smart, user-friendly platform connecting tenants and property owners in Uganda, enabling digital rental applications, lease management, and secure payments.

## Features

### For Tenants
- Search and filter properties
- View listings with rich media and map views
- View live property locations on an interactive map
- Apply online and upload documents
- Track application status
- Sign digital lease agreements
- Pay rent and report maintenance issues

### For Property Owners
- Create and manage listings
- Pin property location using map interface
- Receive and review tenant applications
- Communicate with tenants
- Manage leases and receive rent payments
- Track maintenance requests

## Tech Stack

### Frontend
- Next.js (React framework)
- Tailwind CSS
- React Query / SWR
- Mapbox / Leaflet.js

### Backend
- FastAPI (Python)
- PostgreSQL + PostGIS
- Firebase Auth / Supabase Auth

## Getting Started

### Prerequisites
- Node.js 18+
- Python 3.9+
- PostgreSQL 13+
- Docker (optional)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tenantconnect.git
cd tenantconnect
```

2. Frontend Setup:
```bash
cd frontend
npm install
npm run dev
```

3. Backend Setup:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

4. Database Setup:
```bash
# Create PostgreSQL database
createdb tenantconnect
# Run migrations
cd backend
alembic upgrade head
```

## Development

### Frontend Development
- Run `npm run dev` in the frontend directory
- Access the development server at `http://localhost:3000`

### Backend Development
- Run `uvicorn main:app --reload` in the backend directory
- Access the API documentation at `http://localhost:8000/docs`

## Project Structure

```
tenantconnect/
├── frontend/           # Next.js frontend application
├── backend/           # FastAPI backend application
├── docs/             # Project documentation
└── docker/           # Docker configuration files
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, email support@tenantconnect.ug or join our Slack channel. 