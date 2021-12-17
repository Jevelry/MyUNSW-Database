-- COMP3311 21T3 Ass2 ... extra database definitions
-- add any views or functions you need into this file
-- note: it must load without error into a freshly created mymyunsw database
-- you must submit this even if you add nothing to it

create or replace function
	getTranscript(_id integer) returns setof transcriptrecord 
as $$

begin
    return query
    select 
        s.code, 
        t.code as term, 
        cast(s.name as text), 
        ce.mark, 
        cast(ce.grade as character(2)), 
        s.uoc
    from course_enrolments ce 
        join courses c on (ce.course = c.id)
        join subjects s on (s.id = c.subject)
        join terms t on (t.id = c.term)
    where ce.student = _id
    order by t.id, t.code, s.code
	;
end;

$$
language plpgsql;




create or replace view q2Programs(code, name, uoc, faculty, duration)
as select p.id, p.name, p.uoc, org.longname, p.duration
from programs p
    join orgunits org on (p.offeredby = org.id)
;

create or replace view q2Streams(id, code, name, faculty)
as select s.id, s.code, s.name, org.longname
from streams s
    join orgunits org on (s.offeredby = org.id)
;
