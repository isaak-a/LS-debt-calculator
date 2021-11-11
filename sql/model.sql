CREATE SCHEMA debt_calc_user;

CREATE TABLE debt_calc_user."school_stats" (
    "school" TEXT,
    "percent_get_grant" INTEGER,
    "median_grant" NUMERIC,
    "tuition_semester_res" NUMERIC,
    "tuition_semester_nonres" NUMERIC,
    "fees_semester_res" NUMERIC,
    "fees_semester_nonres" NUMERIC,
    "tuition_credit_res" NUMERIC,
    "tuition_credit_nonres" NUMERIC,
    "fees_credit_res" NUMERIC,
    "fees_credit_nonres" NUMERIC,
    "col_on_campus" NUMERIC,
    "col_off_campus" NUMERIC,
    "col_at_home" NUMERIC,
    "unemployed_not_seeking" INTEGER,
    "unemployed_seeking" INTEGER,
    "total_graduates" INTEGER,
    "school_type" TEXT,
    "grad_credit_hours" NUMERIC,
    "med_salary_private" NUMERIC,
    "med_salary_public" NUMERIC,
    "tuition_year_nonres" NUMERIC,
    "tuition_year_res" NUMERIC,
    "fees_year_nonres" NUMERIC,
    "fees_year_res" NUMERIC
);
