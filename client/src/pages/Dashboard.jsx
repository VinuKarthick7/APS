import { useEffect, useState } from "react";
import { getFacultyDashboard } from "../api/faculty";

export default function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    getFacultyDashboard().then(setData);
  }, []);

  if (!data) return <p>Loading...</p>;

  return (
    <div>
      <h2>Faculty Dashboard</h2>

      <h3>Assignments</h3>
      {data.assignments.map((a, i) => (
        <p key={i}>{a.course_code} - {a.class_name}</p>
      ))}

      <h3>Topics</h3>
      {data.progress.map((p, i) => (
        <p key={i}>{p.topic_title} - {p.status}</p>
      ))}
    </div>
  );
}
