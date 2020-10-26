import React from 'react';
import {
    Link,
    useParams
  } from "react-router-dom";
import { useQuery, useMutation } from 'react-apollo';
import { gql } from 'apollo-boost';

const QUERY_EDUCATIONS = gql`
  query {
    educations {
      id
      name
      educationType
      educationLength
      educationPace
      description
    }
}
`;

const QUERY_EDUCATION_BY_ID = gql`
  query ($id: Int!) {
    educationById(id: $id) {
      id
      name
      educationType
      educationLength
      educationPace
      description
    }
}
`;

export function EducationInfo() {
  const { data, loading } = useQuery(QUERY_EDUCATIONS
  );
  
  if (loading) return <p>Loading...</p>;
   
  return <div className="education-item-wrapper">{data.educations.map(({ id, name, educationType, educationLength, educationPace, description }) => (
    <Link to={`/education/${id}`} id={id} key={id} className="education-item">
        <div>
            <h3>
                {name}
            </h3>
            <div className="info">
                <p>{educationType}</p> <p>{educationLength}</p> <p>{educationPace}</p>
            </div> 
            <p className="description">
                {description}
            </p>
        </div>
    </Link>
  ))}</div>
}

export function EducationInfoPage() {
    const params = useParams();

    const { loading, error, data } = useQuery(QUERY_EDUCATION_BY_ID, {
        variables: { id: params.educationId },
      });
    
      if (loading) {
        return <p>Loading...</p>;
      }
      if (error) {
        console.error(error);
        return "Error!";
      }

    console.log("DATA: " + JSON.stringify(data, null, 2))
    return (
        <div className="education-page">
          <h1 className="m-0">{data.educationById.name}</h1>
          <div className="info"><h3>{data.educationById.educationType}</h3> <h3>{data.educationById.educationLength}</h3> <h3>{data.educationById.educationPace}</h3></div>
          <p className="description">
            {data.educationById.description}
          </p>
        </div>
    )
}

export { QUERY_EDUCATIONS };