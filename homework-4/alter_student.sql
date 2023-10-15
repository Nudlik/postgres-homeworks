-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
CREATE TABLE IF NOT EXISTS public.student
(
    student_id integer NOT NULL DEFAULT nextval('student_student_id_seq'::regclass),
    first_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    birthday date NOT NULL,
    phone character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT student_pkey PRIMARY KEY (student_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.student
      OWNER TO postgres;

-- 2. Добавить в таблицу student колонку middle_name varchar
ALTER TABLE public.student
        ADD COLUMN middle_name character varying(50) COLLATE pg_catalog."default";

-- 3. Удалить колонку middle_name
ALTER TABLE public.student
       DROP COLUMN middle_name;

-- 4. Переименовать колонку birthday в birth_date
ALTER TABLE public.student
     RENAME COLUMN birthday TO birth_date;

-- 5. Изменить тип данных колонки phone на varchar(32)
 ALTER TABLE public.student
ALTER COLUMN phone TYPE varchar(32);

-- 6. Вставить три любых записи с автогенерацией идентификатора
INSERT INTO public.student (first_name, last_name, birth_date, phone)
     VALUES ('A', 'a-a', '1023-10-15', '1234567890'),
            ('B', 'b-b', '1023-10-14', '0987654321'),
            ('C', 'c-c', '1023-10-13', '9876543210');

-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
TRUNCATE TABLE public.student RESTART IDENTITY;
